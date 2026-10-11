import { test } from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import url from "node:url";

const protocolDir = path.dirname(path.dirname(url.fileURLToPath(import.meta.url)));
const modelsDir = path.join(protocolDir, "octobot_protocol_ts", "models");

function read(name) {
  return fs.readFileSync(path.join(modelsDir, name), "utf8");
}

const exists = fs.existsSync(path.join(modelsDir, "MarketMakingConfiguration.ts"));
const skip = !exists;
const reason = skip ? "skipped: codegen output missing — run `npm run generate:typescript` first" : undefined;

test("real codegen output narrows MarketMakingConfiguration.configuration_type", { skip: reason }, () => {
  const src = read("MarketMakingConfiguration.ts");
  assert.match(src, /'configuration_type':\s*'market_making'\s*;/);
  assert.doesNotMatch(src, /'configuration_type'\s*:\s*ActionConfigurationType\b/);
});

test("real codegen output narrows TradingTentaclesConfiguration.configuration_type", { skip: reason }, () => {
  const src = read("TradingTentaclesConfiguration.ts");
  assert.match(src, /'configuration_type':\s*'trading_tentacles'\s*;/);
});

test("real codegen output narrows CreateAutomationConfiguration.action_type", { skip: reason }, () => {
  const src = read("CreateAutomationConfiguration.ts");
  assert.match(src, /'action_type':\s*'automation_create'\s*;/);
});

test("real codegen output narrows SignalBotConfiguration.configuration_type", { skip: reason }, () => {
  const src = read("SignalBotConfiguration.ts");
  assert.match(src, /'configuration_type':\s*'signal_bot'\s*;/);
});

test("real codegen output keeps ActionConfigurationType as full union", { skip: reason }, () => {
  const src = read("ActionConfigurationType.ts");
  assert.match(src, /'market_making'.*'trading_tentacles'.*'copy'.*'generic_process'.*'generic_workflow'.*'signal_bot'/s);
});

test("real codegen output keeps UserActionType as full union", { skip: reason }, () => {
  const src = read("UserActionType.ts");
  assert.match(src, /'automation_create'.*'accounts_refresh'/s);
});

test("real codegen output has no leftover HttpFile import", { skip: reason }, () => {
  const files = fs.readdirSync(modelsDir).filter((f) => f.endsWith(".ts"));
  for (const f of files) {
    assert.doesNotMatch(read(f), /HttpFile/, `${f} still references HttpFile`);
  }
});

test("real codegen output has no Date typings on properties", { skip: reason }, () => {
  const files = fs.readdirSync(modelsDir).filter((f) => f.endsWith(".ts"));
  for (const f of files) {
    assert.doesNotMatch(read(f), /^\s*'[^']+'?\??:\s*Date\b/m, `${f} still has Date property typing`);
  }
});
