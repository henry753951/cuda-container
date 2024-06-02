import { fileURLToPath } from "node:url";

export default defineNuxtConfig({
  shadcn: {
    prefix: "",
  },
  devtools: true,
  app: {
    head: {
      htmlAttrs: {
        lang: "zh-tw",
      },
      title: "CUDA Docker Image Builder",
    },
  },
  components: {
    dirs: ["~/components"],
  },
  alias: {
    images: fileURLToPath(new URL("./assets/images", import.meta.url)),
    styles: fileURLToPath(new URL("./assets/styles", import.meta.url)),
  },

  modules: [
    "@pinia/nuxt",
    "@pinia-plugin-persistedstate/nuxt",
    "@nuxtjs/tailwindcss",
    "shadcn-nuxt",
    "@nuxt/eslint",
    "@vueuse/nuxt",
    "nuxt-icon",
    "dayjs-nuxt",

  ],
});
