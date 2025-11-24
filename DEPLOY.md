# Deploying to Cloudflare Pages

This guide explains how to deploy your optimized portfolio build to Cloudflare Pages.

## Prerequisites

*   **Cloudflare Account:** You need a Cloudflare account.
*   **Node.js & npm:** Required to run the `wrangler` CLI (if deploying via command line).

## Option 1: Command Line Deployment (Recommended)

This method uses `wrangler`, Cloudflare's CLI tool. You don't need to install it globally; we can use `npx`.

1.  **Login to Cloudflare:**
    Run the following command and follow the browser prompts to authorize:
    ```bash
    npx wrangler login
    ```

2.  **Deploy the Build Folder:**
    Run the following command to deploy the `build` directory to your project `bmanick-dev`:
    ```bash
    npx wrangler pages deploy build --project-name bmanick-dev
    ```
    *   If the project doesn't exist, Wrangler will ask to create it.
    *   It will ask for a production branch name (usually `main` or `master`).

3.  **Verify Deployment:**
    Once complete, Wrangler will output a URL (e.g., `https://bmanick-dev.pages.dev`). You can map your custom domain `bmanick.dev` in the Cloudflare Dashboard under **Pages > Custom Domains**.

## Option 2: Manual Upload (Cloudflare Dashboard)

1.  **Log in** to the [Cloudflare Dashboard](https://dash.cloudflare.com/).
2.  Go to **Workers & Pages** > **Create application** > **Pages** > **Upload assets**.
3.  **Project Name:** Enter `bmanick-dev`.
4.  **Upload:** Drag and drop the **`build`** folder (make sure you generated it first with `python3 build.py`) into the upload area.
5.  **Deploy:** Click **Deploy Site**.

## Option 3: Git Integration (Continuous Deployment)

1.  Push your code to a GitHub/GitLab repository.
2.  Log in to Cloudflare Dashboard > **Workers & Pages** > **Create application** > **Pages** > **Connect to Git**.
3.  Select your repository.
4.  **Build Settings:**
    *   **Build command:** `python3 build.py`
    *   **Build output directory:** `build`
5.  **Save and Deploy.** Cloudflare will now automatically build and deploy whenever you push changes.
