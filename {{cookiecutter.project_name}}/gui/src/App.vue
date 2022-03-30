<template>
  <v-app>
    <AppBar />

    <v-main>
      <Develop v-if="true" />
      <router-view />
      <Alert />
    </v-main>
  </v-app>
</template>

<script>
import Alert from "./App/Alert";
import AppBar from "./App/AppBar";
import Develop from "./App/Develop";

export default {
  name: "App",
  components: { Alert, AppBar, Develop },
};
</script>
