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
import TestFunctions from "./components/Home/TestFunctions";
import Plot from "./components/Home/Plot";
import Styling from "./components/Home/Styling";
import Usable from "./components/Home/Usable";

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
