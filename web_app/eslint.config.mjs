import withNuxt from "./.nuxt/eslint.config.mjs";
import pluginVue from "eslint-plugin-vue";

export default withNuxt([
  ...pluginVue.configs["flat/strongly-recommended"],
  {
    rules: {
      "vue/max-attributes-per-line": [
        "error",
        {
          singleline: {
            max: 1,
          },
          multiline: {
            max: 1,
          },
        },
      ],
      "vue/multi-word-component-names": "off",
    },
  },
]);
