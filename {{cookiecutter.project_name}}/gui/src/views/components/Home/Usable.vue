<template>
  <div class="ma-16">
    <h2>Some other functions / features you could use</h2>
    <p>Scroll to bottom (call me after content update)</p>
    <v-btn class="mb-8" @click="$store.commit('scrollToBottom')">Scroll</v-btn>
    <p>Any py function that will fail, report it on GUI</p>
    <v-btn class="mb-8" @click="bad_function">Bad function</v-btn>
  </div>
</template>

<script>
import { mapFields } from "vuex-map-fields";
import { mapState } from "vuex";

export default {
  computed: {
    ...mapState("settings", ["selected_index"]), // This is syntax how to import variables from store module
    ...mapFields(["test1"]),
  },
  methods: {
    bad_function() {
      window.eel.test_function("fail")((result) => {
        console.log("It should fail.", result);
      });
    },
  },
};
</script>
