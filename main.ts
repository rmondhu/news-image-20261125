// Entry runner — "THE WORLD TODAY", Wednesday 25 November 2026.
//
// The front page is already finished and sits next to this file as
// entry.png; it was painted at build time from render.html in a
// headless browser. When the grader runs this program, all it has to
// do is check that the picture is the one the competition asks for
// and hand over an exact copy. Nothing is downloaded, nothing is
// drawn, nothing reads the clock, so two runs always agree exactly.
//
//   MAKEFUN_OUTPUT_DIR=out node main.ts
//
// The destination defaults to /output when the variable is unset.

import * as crypto from "node:crypto";
import * as fs from "node:fs";
import * as path from "node:path";
import { fileURLToPath } from "node:url";

const WANT_SIDE = 1024;
const WANT_BYTES = 1024 * 1024;
const FILE_NAME = "entry.png";

// A PNG always opens with these eight bytes.
const PNG_MAGIC = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);

function fail(message: string): never {
  console.error(`entry runner: ${message}`);
  process.exit(1);
}

function here(): string {
  return path.dirname(fileURLToPath(import.meta.url));
}

function readEntry(): Buffer {
  const file = path.join(here(), FILE_NAME);
  if (!fs.existsSync(file)) fail(`no ${FILE_NAME} next to main.ts`);
  return fs.readFileSync(file);
}

function dimensions(bytes: Buffer): [number, number] {
  if (bytes.length < 33 || !bytes.subarray(0, 8).equals(PNG_MAGIC)) {
    fail("entry.png does not start with the PNG magic bytes");
  }
  if (bytes.toString("latin1", 12, 16) !== "IHDR") {
    fail("entry.png has no IHDR chunk in first position");
  }
  const width = bytes.readUInt32BE(16);
  const height = bytes.readUInt32BE(20);
  return [width, height];
}

function main(): void {
  const bytes = readEntry();
  const [width, height] = dimensions(bytes);
  if (width !== WANT_SIDE || height !== WANT_SIDE) {
    fail(`entry.png is ${width}x${height}, want ${WANT_SIDE}x${WANT_SIDE}`);
  }
  if (bytes.length > WANT_BYTES) {
    fail(`entry.png is ${bytes.length} bytes, over the ${WANT_BYTES} cap`);
  }
  const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
  const outFile = path.join(outDir, FILE_NAME);
  fs.mkdirSync(outDir, { recursive: true });
  fs.writeFileSync(outFile, bytes);
  const sha = crypto.createHash("sha256").update(bytes).digest("hex");
  console.log(`wrote ${outFile} — ${bytes.length} bytes, ${width}x${height}, sha256 ${sha}`);
}

main();
