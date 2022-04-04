{% raw -%}
<template>
  <v-container id="app" class="mb-10">
    <v-row>
      <v-col cols="4" class="d-flex justify-center align-center text-center">
        <TestFunctions />
      </v-col>
      <v-col cols="4">
        <Plot />
      </v-col>
      <v-col cols="4" class="d-flex align-center justify-center text-center">
        <Styling />
      </v-col>
    </v-row>
    <Usable />
  </v-container>
</template>

<script>
import TestFunctions from "./layout/TestFunctions";
import Plot from "./layout/Plot";
import Styling from "./layout/Styling";
import Usable from "./layout/Usable";

export default {
  components: {
    TestFunctions,
    Plot,
    Styling,
    Usable,
  },
};
</script>

<style></style>
{%- endraw %}
