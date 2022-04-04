{% raw -%}
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
import Alert from "./layout/Alert";
import AppBar from "./layout/AppBar";
import Develop from "./layout/Develop";

export default {
  name: "App",
  components: { Alert, AppBar, Develop },
};
</script>
{%- endraw %}
