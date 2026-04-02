import { AlertTriangle, Lock, LockOpen, ShieldCheck } from "lucide-react"
import { useEffect, useState } from "react"

import type { Task_Output as Task } from "@/client"
import { NodesService } from "@/client"
import { Button } from "@/components/ui/button"
import { LoadingButton } from "@/components/ui/loading-button"
import { getTemplateById } from "@/lib/action-templates"
import type { ActionRow } from "./ColumnMappingStep"

export interface EncryptStepProps {
  actions: ActionRow[]
  onImport: (tasks: Task[]) => void
  onBack: () => void
  isImporting: boolean
}

const ENCRYPTION_ENV_VARS = [
  "TASKS_INPUTS_RSA_PRIVATE_KEY",
  "TASKS_INPUTS_ECDSA_PUBLIC_KEY",
  "TASKS_OUTPUTS_RSA_PUBLIC_KEY",
  "TASKS_OUTPUTS_ECDSA_PRIVATE_KEY",
  "TASKS_INPUTS_RSA_PUBLIC_KEY",
  "TASKS_INPUTS_ECDSA_PRIVATE_KEY",
  "TASKS_OUTPUTS_RSA_PRIVATE_KEY",
  "TASKS_OUTPUTS_ECDSA_PUBLIC_KEY",
]

function getValidActions(actions: ActionRow[]): ActionRow[] {
  return actions.filter((action) => {
    const template = getTemplateById(action.templateId)
    if (!template) return false
    return template.params.every(
      (p) => !p.required || action.paramValues[p.key]?.trim(),
    )
  })
}

export default function EncryptStep({
  actions,
  onImport,
  onBack,
  isImporting,
}: EncryptStepProps) {
  const [encryptionEnabled, setEncryptionEnabled] = useState<boolean | null>(null)
  const validActions = getValidActions(actions)

  useEffect(() => {
    NodesService.getNodeConfig()
      .then((data) => setEncryptionEnabled((data as { tasks_encryption_enabled?: boolean }).tasks_encryption_enabled ?? false))
      .catch(() => setEncryptionEnabled(false))
  }, [])

  const buildPlaintextTasks = (): Task[] =>
    validActions.map((action) => ({
      name: action.name,
      content: JSON.stringify(action.paramValues),
      type: "execute_actions",
    }))

  const handleImportWithEncryption = async () => {
    const contents = validActions.map((action) =>
      JSON.stringify(action.paramValues),
    )

    const username = localStorage.getItem("auth_username") || "node"
    const password = localStorage.getItem("auth_password") || ""
    const res = await fetch("/api/v1/tasks/encrypt-content", {
      method: "POST",
      headers: {
        Authorization: `Basic ${btoa(`${username}:${password}`)}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ contents }),
    })

    if (!res.ok) {
      throw new Error("Encryption failed")
    }

    const encrypted: { content: string; content_metadata: string }[] = await res.json()

    const tasks: Task[] = validActions.map((action, i) => ({
      name: action.name,
      content: encrypted[i].content,
      content_metadata: encrypted[i].content_metadata,
      type: "execute_actions",
    }))

    onImport(tasks)
  }

  const handleImportWithoutEncryption = () => {
    onImport(buildPlaintextTasks())
  }

  return (
    <div className="flex flex-col gap-6">
      <div>
        <p className="text-sm font-medium">
          Encrypt & Import
        </p>
        <p className="text-xs text-muted-foreground">
          Encryption adds an additional security layer by protecting all action parameters before they are stored.
        </p>
      </div>

      {encryptionEnabled === null ? (
        <p className="text-sm text-muted-foreground">Checking encryption status...</p>
      ) : encryptionEnabled ? (
        <div className="flex flex-col gap-4">
          <div className="flex items-start gap-3 rounded-lg border border-green-500/30 bg-green-500/5 p-4">
            <ShieldCheck className="size-5 text-green-500 mt-0.5 shrink-0" />
            <div>
              <p className="text-sm font-medium">Encryption is enabled</p>
              <p className="text-xs text-muted-foreground mt-1">
                Task content will be encrypted before submission using the same hybrid
                encryption as the Python CSV tools (AES-256-GCM + RSA-4096 + ECDSA).
              </p>
            </div>
          </div>

          <div className="flex gap-2 justify-end">
            <Button variant="outline" onClick={onBack} disabled={isImporting}>
              Back
            </Button>
            <LoadingButton
              loading={isImporting}
              onClick={handleImportWithEncryption}
              disabled={validActions.length === 0}
            >
              <Lock className="size-3.5 mr-1.5" />
              Import {validActions.length} Action{validActions.length !== 1 ? "s" : ""}
            </LoadingButton>
          </div>
        </div>
      ) : (
        <div className="flex flex-col gap-4">
          <div className="flex items-start gap-3 rounded-lg border border-yellow-500/30 bg-yellow-500/5 p-4">
            <AlertTriangle className="size-5 text-yellow-500 mt-0.5 shrink-0" />
            <div>
              <p className="text-sm font-medium">Encryption is not configured</p>
              <p className="text-xs text-muted-foreground mt-1">
                Set the following environment variables and restart the application to enable task encryption:
              </p>
              <ul className="text-xs font-mono text-muted-foreground mt-2 ml-4 list-disc space-y-0.5">
                {ENCRYPTION_ENV_VARS.map((v) => (
                  <li key={v}>{v}</li>
                ))}
              </ul>
            </div>
          </div>

          <div className="flex gap-2 justify-end">
            <Button variant="outline" onClick={onBack} disabled={isImporting}>
              Back
            </Button>
            <LoadingButton
              loading={isImporting}
              variant="secondary"
              onClick={handleImportWithoutEncryption}
              disabled={validActions.length === 0}
            >
              <LockOpen className="size-3.5 mr-1.5" />
              Import {validActions.length} Action{validActions.length !== 1 ? "s" : ""}
            </LoadingButton>
          </div>
        </div>
      )}
    </div>
  )
}
