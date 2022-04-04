{% raw -%}
<template>
  <v-container>
    <v-row align="center" justify="center">
      <v-col cols="10">
        <h1>Help</h1>
      </v-col>
    </v-row>
    <v-row align="center" justify="center">
      <v-col cols="9">
        <!--           -->
        <!-- LOAD DATA -->
        <!--           -->

        <h2>Lorem</h2>
        <v-divider class="mt-1 mb-4"></v-divider>
        <p class="blockquote">
          Vivamus porttitor turpis ac leo. Phasellus enim erat, vestibulum vel, aliquam a, posuere eu, velit.
          Etiam quis quam. Nulla turpis magna, cursus sit amet, suscipit a, interdum id, felis. Ut enim ad
          minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        </p>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "Home",

  data: () => ({
    center: "center",
  }),
};
</script>

<style>
h2 {
  margin-top: 30px;
}
</style>
{%- endraw %}
