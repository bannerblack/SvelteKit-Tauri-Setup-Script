# Sveltekit + Tauri Setup Script

This project automates the creation of a Sveltekit + Tauri project using the default Sveltekit and Tauri command line tools, meaning you are always installing with the most up-to-date packages and generated files.

#### This script:

- Creates a SvelteKit project using `sv create`
- Adds packages available within the interactive version of `sv create` (customize: [SvelteKit docs](https://svelte.dev/docs/cli/sv-add))
  - Note: adapter-static is required
- Adds Tauri CLI tool and Tauri JS API packages (for using Tauri invoke, etc.)
- Installs dependencies with npm
- Creates a Tauri project and customizes it for use with Sveltekit using `tauri init`
- Adds a layout.ts file at the root route with `prerendering = true` and `ssr = false`

## How to Use

If you haven't already, install:

- Node JS
- Rust and dependencies
- Tauri dependencies (will vary depending on if you're using windows, linux, or macOs)

### 1. Run the Script

#### Manually

1.  Set the `default_project_root` variable in the script to the location you want to install the project (this folder will be the root)

2.  Run:

```bash
python ./setup-sv-tauri.py
```

#### Run from Command Line

1. Run:

```bash
python ./setup-sv-tauri.py "path/to/folder"
```

#### Optionally:

- Delete, then remake the project folder specified if it exists using the `--clean` flag:

```bash
python ./setup-sv.tauri.py "path/to/folder" --clean
```

### 2. Edit /src-tauri/tauri.conf.json

- Edit the unique identifier in tauri.conf.json
- (Optionally) Edit the window and app name from the default (folder name)

### 3. Run the project in dev mode

Run from root

```bash
- Run from root folder
npx tauri dev
```

```bash
- Run from /src-tauri folder
cargo tauri dev
```

### 4. Build

```bash
- Build from root folder
npx tauri build
```

```bash
- Build from root folder
cargo tauri build
```

---

#### Default Add-ons for Svelte project:

- Prettier
- Eslint
- TailwindCSS (+typography/forms)
- Vitest
- Adapter-Static (required for Tauri)
- mdsvex

---

Feel free to fork and customize!
