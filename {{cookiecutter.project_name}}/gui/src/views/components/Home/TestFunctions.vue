{% raw %}
<template>
  <div>
    <h3>Flex column</h3>

    <div class="d-flex flex-column">
      <v-btn @click="$store.commit('test_mutation')" class="ma-4"> Test mutation </v-btn>

      <v-btn @click="$store.commit('clear_state')" class="ma-4"> Test clear_state </v-btn>

      <v-btn @click="edit_state" class="ma-4"> Local method </v-btn>

      <p>{{ test1 }}</p>
    </div>
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
    edit_state() {
      this.test1 = 999; // You can edit variable from vuex store if imported with mapFields
    },
  },
};
</script>

{% endraw %}
