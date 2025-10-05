# Sveltekit + Tauri Setup Script

This project automates the creation of a SvelteKit + Tauri project using the default Sveltekit and Tauri command line tools, meaning you are always setting up with the most up-to-date packages and generated files.

#### This script:

1. Creates a SvelteKit project using `sv create`
   1.Adds packages available within the interactive version of `sv create` using `sv add` (customization details here: [SvelteKit docs](https://svelte.dev/docs/cli/sv-add))

   - Note: adapter-static is required

1. Adds Tauri CLI tool and Tauri JS API packages (for using Tauri invoke, etc.)
1. Installs dependencies with npm
1. Creates a Tauri project and customizes it for use with Sveltekit using `tauri init`
1. Adds a layout.ts file at the root route with `prerendering = true` and `ssr = false`

## How to Use

If you haven't already, install:

- [Node JS](https://nodejs.org/en)
- [Rust](https://rust-lang.org/)
- [Tauri dependencies](https://v2.tauri.app/start/prerequisites/) (will vary depending on if you're using windows, linux, or macOs)

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

**Note:** The `--clean` flag will delete and remake the provided project dir

### 2. Edit /src-tauri/tauri.conf.json

- Edit the unique identifier in tauri.conf.json to match your project
- (Optionally) Edit the window and app name from the default, which is your folder name

### 3. Run the project in dev mode

```bash
# Run from root folder
npx tauri dev
```

```bash
# Run from /src-tauri/ folder
cargo tauri dev
```

### 4. Build

```bash
# Build from root folder
npx tauri build
```

```bash
# Build from /src-tauri/ folder
cargo tauri build
```

---

#### Default add-ons for SvelteKit project (set in script):

- Prettier
- ESlint
- TailwindCSS (+typography/forms)
- Vitest
- Adapter-Static (required for Tauri)
- mdsvex

---

### Contribute

Feel free to fork and customize or contribute by adding a script for another language!
