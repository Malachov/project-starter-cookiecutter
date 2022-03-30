<template>
  <v-app-bar class="ma-4" flat max-height="120px" color="transparent">
    <img class="ma-5" src="./../assets/img/logo.png" height="70" />

    <v-spacer></v-spacer>

    <Settings />

    <v-btn
      v-if="help_switch"
      v-on:click="help_switch = !help_switch"
      icon
      :color="color_help"
      @mouseover="color_help = 'pink lighten-3'"
      @mouseleave="color_help = ''"
      to="/help"
      class="ma-4"
    >
      <v-icon size="50">mdi-help-circle</v-icon>
    </v-btn>

    <v-btn
      v-if="!help_switch"
      v-on:click="help_switch = !help_switch"
      icon
      :color="color_help"
      @mouseover="color_help = 'pink lighten-3'"
      @mouseleave="color_help = ''"
      to="/"
      class="ma-4"
    >
      <v-icon size="50">mdi-home</v-icon>
    </v-btn>
  </v-app-bar>
</template>

<script>
import Settings from "./Settings";
export default {
  components: { Settings },

  data: () => ({
    help_switch: 1,
    color_load: "",
    color_home: "",
    color_help: "",
  }),
};
</script>
