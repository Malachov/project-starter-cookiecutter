{% raw -%}
<template>
  <v-container>
    <h1>Development</h1>
    <p>
      Turn me off in App.vue, do not delete me. Do all development here to not messing working components.
    </p>
    <v-btn @click="run">Function performance</v-btn>

    <h2 v-if="timeit" class="mt-4">It takes {{ timeit }}</h2>
  </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";
import { mapFields } from "vuex-map-fields";

export default {
  data: () => ({
    timeit: null,
  }),

  computed: {
    // Use mapFields if you want to read and also edit global variables
    ...mapFields(["delayed"]),
    ...mapFields("settings", ["delayed"]), // If acessing module

    // Use mapState if you want only read
    ...mapState,
  },

  methods: {
    // If you need to use some action
    ...mapActions(["nameOfAction"]),

    run() {
      let start = new Date();

      window.eel.test_function({})(() => {
        let end = new Date();
        this.timeit = (end - start) / 1000;
      });
    },
  },
};
</script>
{%- endraw %}
