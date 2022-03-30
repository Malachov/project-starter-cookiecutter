<template>
  <v-container>
    <Plotly
      v-if="show_data_loaded_plot"
      :data="plot_data"
      :layout="{ ...plot_layout, height: 550 }"
      class="mt-4"
    ></Plotly>
  </v-container>
</template>

<script>
import { mapState } from "vuex";
import { Plotly } from "vue-plotly";

export default {
  components: { Plotly },

  computed: {
    ...mapState(["plot_data", "plot_layout", "show_data_loaded_plot"]),
  },

  // This will run when component created
  mounted() {
    this.$store.dispatch("test_action", { arg1: 666 });
  },
};
</script>
