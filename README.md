# Sveltekit + Tauri Setup Script

This project automates the creation of a [SvelteKit](https://svelte.dev/docs/kit/introduction) + [Tauri](https://v2.tauri.app/) project using the default SvelteKit and Tauri command line tools, ensuring you are always setting up with the most up-to-date packages and official generated files.

#### This script:

1. Creates a SvelteKit project using `sv create`
1. Adds packages available within the interactive version of `sv create` using `sv add` (customization details here: [SvelteKit docs](https://svelte.dev/docs/cli/sv-add))

   - Note: **adapter-static** is required

1. Adds Tauri CLI tool and Tauri JS API packages (for using Tauri invoke, etc.)
1. Installs dependencies with `npm`
1. Creates a Tauri project and customizes it for use with Sveltekit using `tauri init`
1. Adds a layout.ts file in the root route with `prerendering = true` and `ssr = false`

##### Soft Opinions

- Uses `npm`
- Installs specific SvelteKit add-ons from the official CLI tool (see below for list)
- Python required to run script

## How to Use

If you haven't already, install:

- [Node JS](https://nodejs.org/en)
- [Rust](https://rust-lang.org/)
- [Tauri dependencies](https://v2.tauri.app/start/prerequisites/) (will vary depending on if you're developing on windows, linux, or macOS)

### 1. Run the Script

#### Manually

1.  Set the `default_project_root` variable in the script to the location you want to install the project (this folder will be the root)

2.  Run:

```bash
python ./setup-sv-tauri.py
```

#### (OR) Run from Command Line

```bash
python ./setup-sv-tauri.py "path/to/folder"
```

**Note:** The `--clean` flag will delete and remake the provided project dir

---

### 2. Edit /src-tauri/tauri.conf.json

- Edit the unique identifier in tauri.conf.json to match your project
- (Optionally) Edit the window and app name from the default, which is your folder name

---

### 3. Run the project in dev mode

```bash
# Run from root folder
npx tauri dev
```

```bash
# Run from /src-tauri/ folder
cargo tauri dev
```

---

### 4. Build

```bash
# Build from root folder
npx tauri build
```

```bash
# Build from /src-tauri/ folder
cargo tauri build
```

Done!

---

#### Default settings and add-ons for SvelteKit project (set in script):

- Typescript
- Minimal project scaffolding
- Prettier
- ESlint
- TailwindCSS (+typography/forms)
- Vitest
- Adapter-Static (required for Tauri)
- mdsvex

---

### Notes About Sveltekit and Tauri

If you haven't used SvelteKit with Tauri before, you should know that this method requires Sveltekit projects to be rendered statically, which disables use of any server-side (SSR) functionality. You will essentially be using Tauri and Rust as your backend for things like authentication and database management. The plus side is that Rust is an extremely performant language and can do anything you could do with SSR, just with a little less convenience. Of course, it also gives you local file access, which is a huge benefit if it fits your use case.

Generally speaking:

- Use load functions to get data in layout.ts and page.ts files
- Use client-side form validation with tauri invoke to submit forms and perform CRUD operations
- Use Tauri stores for persistent data like user settings

---

## Project Tree

📦SvelteTauri-App  
┣ 📂src  
┃ ┣ 📂lib  
┃ ┣ 📂routes  
┃ ┃ ┣ 📜+layout.svelte  
┃ ┃ ┣ 📜+layout.ts  
┃ ┃ ┗ 📜+page.svelte  
┃ ┣ 📜app.css  
┃ ┣ 📜app.d.ts  
┃ ┣ 📜app.html  
┃ ┗ 📜demo.spec.ts  
┣ 📂src-tauri  
┃ ┣ 📂capabilities  
┃ ┣ 📂icons  
┃ ┣ 📂src  
┃ ┃ ┣ 📜lib.rs  
┃ ┃ ┗ 📜main.rs  
┃ ┣ 📜.gitignore  
┃ ┣ 📜build.rs  
┃ ┣ 📜Cargo.toml  
┃ ┗ 📜tauri.conf.json  
┣ 📂static  
┣ 📜.gitignore  
┣ 📜.npmrc  
┣ 📜.prettierignore  
┣ 📜.prettierrc  
┣ 📜eslint.config.js  
┣ 📜package-lock.json  
┣ 📜package.json  
┣ 📜README.md  
┣ 📜svelte.config.js  
┣ 📜tsconfig.json  
┗ 📜vite.config.ts

---

### Contribute

Feel free to fork and customize or contribute by adding a script for another language!
