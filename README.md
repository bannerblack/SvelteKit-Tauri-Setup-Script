# Sveltekit + Tauri Setup Script

This project automates the creation of a Sveltekit + Tauri project using the default Sveltekit and Tauri command line tools, meaning you are always installing with the most up-to-date packages and generate files.

#### This script:

- Creates a sveltekit project using `sv create`
- Adds packages available within the interactive version of of `sv create` (customize: https://svelte.dev/docs/cli/sv-add)
  - Note: adapter-static is required
- Adds Tauri CLI tool and Tauri JS API (for using Tauri invoke, etc.)
- Installs dependencies with npm
- Creates a Tauri project and customizes it for use with Sveltekit using `tauri init`
- Adds a layout.ts file at the root route with `prerendering = true` and `ssr = false`

## How to Use

If you haven't already, install:

- Node JS
- Rust and dependencies
- Tauri dependencies (will vary depending on if you're using windows, linux, or Macos)

### Run Manually

1.  Set the `default_project_root` variable in the script to the location you want to install the project (this folder will be the root)

2.  Run:

```python
python ./setup-sv-tauri.py
```

### Run from Command Line

1. Run:

```python
python ./setup-sv-tauri.py "path/to/folder"
```

#### Optionally:

- Delete, then remake the project folder specified if it exists:

```python
python ./setup-sv.tauri.py "path/to/folder" --clean
```

### Edit tauri.conf.json

- Edit the unique identifier in tauri.conf.json
- (Optionally) Edit the window and app name from the default (folder name)

### Run

Run from root

```bash
npx tauri dev
```

or Run from src-tauri

```bash
cargo tauri dev
```

### Build

```bash
npx tauri build
```

```bash
cargo tauri build
```

##

Default Add-ons for Svelte project:

- Prettier
- Eslint
- TailwindCSS (+typography/forms)
- Vitest
- Adapter-Static (required for Tauri)
- mdsvex

---

Feel free to fork and customize!
