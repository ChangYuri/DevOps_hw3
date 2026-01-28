// eslint.config.js
import js from "@eslint/js";
import { defineConfig } from "eslint/config";

export default defineConfig([
	{
		files: ["**/*.js"],
        ignores: [
        "**/node_modules/**",
        "**/.history/**",
        "**/.venv/**",
        "**/dist/**",
        "**/build/**",
        ],
		plugins: {
			js,
		},
		extends: ["js/recommended"],
		rules: {
			"no-unused-vars": "warn",
		},
	},
]);

// I use this template from official website 
// And added the ignores