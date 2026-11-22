#!/bin/bash
# Copies the fictional fixture into the empty workspace (runs only with --scaffold).
set -e
cp -R "$(dirname "$0")/../fixtures/lumen-catalogue/." .
rm -f designer.md .keep ux-patterns/.keep
