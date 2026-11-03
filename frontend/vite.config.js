import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

export default defineConfig({
  plugins: [vue()],
  server: {
    proxy: {
      // 🎯 拦截以 /api 开头的请求，转发给 Django
      "/api": {
        target: "http://127.0.0.1:8000", // 你的后端地址
        changeOrigin: true,
      },
    },
  },
});
