import Vue from "vue";
import App from "./App.vue";
import vuetify from "./plugins/vuetify";
import "@mdi/font/css/materialdesignicons.css";
import "./assets/my_css.css";
import router from "./router";
import store from "./store";

// If using as web app, comment it and use google fonts in public index.html
import "./assets/font.css";

// Optionally
import VueFormulate from "@braid/vue-formulate";
import "./assets/formulate.css";

// Own functions
import { create_alert } from "@/assets/js/py_js";

Vue.use(VueFormulate);

// Expose all functions that should be callable from python here
window.eel.expose(create_alert, "create_alert");

if (process.env.NODE_ENV == "development") {
  try {
    window.eel.set_host("ws://localhost:8686");
  } catch (error) {
    document.getElementById("app").innerHTML =
      "Py side is not running. Start app.py with debugger.";
    console.error(error);
  }

  Vue.config.productionTip = true;
  Vue.config.devtools = true;
} else {
  Vue.config.productionTip = false;
  Vue.config.devtools = false;
}

new Vue({
  vuetify,
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
