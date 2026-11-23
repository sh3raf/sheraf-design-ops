#!/bin/bash
# Runs the native `claude plugin eval` suite on a temp copy of the plugin with tests/plugin-evals as its
# evals/, so the published plugin folder holds no scripts (the directory rejects them).
# Extra arguments go to `claude plugin eval`, e.g. --case ux-no-evidence --model sonnet.
set -e
root="$(cd "$(dirname "$0")/.." && pwd)"
tmp="$(mktemp -d)"
cp -R "$root/plugins/sdops/." "$tmp/"
cp -R "$root/tests/plugin-evals" "$tmp/evals"
cd "$tmp"
claude plugin eval . --scaffold --allow-tools Write Edit --trust-plugin --no-publish \
  --output-dir "$root/tests/plugin-evals/results/$(date +%Y%m%dT%H%M%S)" "$@"
