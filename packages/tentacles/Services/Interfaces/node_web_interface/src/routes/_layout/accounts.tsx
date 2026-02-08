import { createFileRoute } from "@tanstack/react-router"
import { Plus } from "lucide-react"
import { useMemo, useState } from "react"

import { CollectionHeader } from "@/components/Common/CollectionHeader"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"

type AccountType = "exchange" | "wallet" | "integration"

type Account = {
  id: string
  name: string
  type: AccountType
  status: "connected" | "pending"
}

const accounts: Account[] = [
  { id: "binance", name: "Binance", type: "exchange", status: "connected" },
  { id: "coinbase", name: "Coinbase", type: "exchange", status: "pending" },
  { id: "ledger", name: "Ledger", type: "wallet", status: "connected" },
  { id: "telegram", name: "Telegram", type: "integration", status: "connected" },
]

const filters = [
  { value: "all", label: "All" },
  { value: "exchange", label: "Exchanges" },
  { value: "wallet", label: "Wallets" },
  { value: "integration", label: "Integrations" },
]

function ManageAccounts() {
  const [searchValue, setSearchValue] = useState("")
  const [filterValue, setFilterValue] = useState("all")

  const filtered = useMemo(() => {
    const query = searchValue.trim().toLowerCase()
    return accounts.filter((account) => {
      const matchesFilter =
        filterValue === "all" ? true : account.type === filterValue
      const matchesQuery = query
        ? `${account.name} ${account.type}`.toLowerCase().includes(query)
        : true
      return matchesFilter && matchesQuery
    })
  }, [filterValue, searchValue])

  return (
    <div className="flex flex-col gap-8">
      <CollectionHeader
        title="Manage accounts"
        description="Connect exchanges, wallets, and integrations."
        action={
          <Button size="lg">
            <Plus className="size-4" />
            Add account
          </Button>
        }
        searchValue={searchValue}
        onSearchChange={setSearchValue}
        searchPlaceholder="Search accounts..."
        filters={filters}
        filterValue={filterValue}
        onFilterChange={setFilterValue}
      />
      {filtered.length === 0 ? (
        <Card className="border-dashed">
          <CardHeader>
            <CardTitle>No accounts found</CardTitle>
            <CardDescription>Try another filter or search.</CardDescription>
          </CardHeader>
        </Card>
      ) : (
        <div className="grid gap-4 md:grid-cols-2">
          {filtered.map((account) => (
            <Card key={account.id} className="transition-shadow hover:shadow-md">
              <CardHeader>
                <div className="flex items-start justify-between gap-3">
                  <div>
                    <CardTitle>{account.name}</CardTitle>
                    <CardDescription className="capitalize">
                      {account.type}
                    </CardDescription>
                  </div>
                  <Badge variant={account.status === "connected" ? "default" : "secondary"}>
                    {account.status}
                  </Badge>
                </div>
              </CardHeader>
              <CardContent className="text-sm text-muted-foreground">
                Manage credentials, permissions, and sync status.
              </CardContent>
            </Card>
          ))}
        </div>
      )}
    </div>
  )
}

export const Route = createFileRoute("/_layout/accounts")({
  component: ManageAccounts,
  head: () => ({
    meta: [{ title: "Manage accounts" }],
  }),
})
