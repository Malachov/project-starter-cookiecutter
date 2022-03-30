import Vue from "vue";
import Vuex from "vuex";

import { getField, updateField } from "vuex-map-fields";
import { return_plot } from "@/assets/js/my";

import settings from "./modules/settings";

Vue.use(Vuex);

// If it's not the first time you are using it, you can bulk edit comment help to have clean code                                      // **DELETELINE
// For example in VS Code, select some **DELETELINE, than hold ctrl + D after every is selected,                                       // **DELETELINE
// use ctrl + L to select all lines and use delete                                                                                     // **DELETELINE
//                                                                                                                                     // **DELETELINE
// These are globel variables and methods that you can access (and also edit) from any component                                       // **DELETELINE
//                                                                                                                                     // **DELETELINE
// How to use from components                                                                                                          // **DELETELINE
//                                                                                                                                     // **DELETELINE
// Import with map or call global                                                                                                      // **DELETELINE
// this.$store.dispatch("action", { param: false });                                                                                   // **DELETELINE
// Check Develop.vue for examples                                                                                                      // **DELETELINE

export default new Vuex.Store({
  strict: false,

  // These are global variables                                                                                                        // **DELETELINE
  state: {
    alert: {
      show: false,
      caption: "",
      message: "",
      error: "",
      type: "",
    },
    test1: 5415, // **DELETELINE
    plot_data: [],
    show_data_loaded_plot: false,
    plot_layout: {
      margin: { l: 50, r: 50, b: 0, t: 40, pad: 8 },
      font: {
        family: "roboto",
      },
      legend: {
        orientation: "h",
        y: -0.2,
      },
      hovermode: "closest",
      height: 1000,
    },
  },

  // If you need to transform data before loading                                                                                     // **DELETELINE
  getters: {
    getField,
  },

  // These are synchronous methods if editing state variables (nice in vue.js dev tools where all variables in each state are saved)
  mutations: {
    // You can edit state var just with asigning if using in component - Check TestFunctions ho to implement                         // **DELETELINE
    updateField,

    // General action to change any property with commit('mutate', ['state_var', 'value'])                                           // **DELETELINE
    mutate(state, payload) {
      state[payload[0]] = payload[1];
    },

    alert(state, { caption, message, error, type }) {
      state.alert = {
        show: true,
        caption: caption,
        message: message,
        error: error,
        type: type,
      };
    },

    // Sometime you need to do rollback or reset of many variables at once
    clear_state(state) {
      state.test1 = "";
    },

    test_mutation(state) {
      // **DELETELINE
      // **DELETELINE
      // **DELETELINE
      state.test1 = 666; // **DELETELINE
    }, // **DELETELINE

    plot_data(state, plot_data) {
      state.plot_data = return_plot(plot_data);
      state.show_data_loaded_plot = true;
    },

    scrollToBottom() {
      window.scrollTo({
        top: document.body.scrollHeight,
        left: 0,
        behavior: "smooth",
      });
      // document.getElementById("app").scrollIntoView({ behavior: "smooth" });
    },
  },

  actions: {
    // Check how to call the function in Plot.vue                                                                                   // **DELETELINE
    test_action({ state, commit }, payload) {
      // Supposed payload structure and default args                                                                                // **DELETELINE
      var payload_default = { arg1: true, arg2: true, arg3: [123, "123"] }; // **DELETELINE
      payload = { ...payload_default, ...payload }; // **DELETELINE
      //                                                                                                                            // **DELETELINE
      // Call python functions that return values with callback with such a syntax                                                  // **DELETELINE
      // You can pass positional arguments or kwargs or pack all settings into one object                                           // **DELETELINE
      window.eel.test_function(payload, { arg2: payload.arg2 })((result) => {
        //                                                                                                                          // **DELETELINE
        // Simple small changes you can do directly with                                                                            // **DELETELINE
        state.test1 = 777; // **DELETELINE
        // If editting more values at once, or using some frequent change, use some mutation                                        // **DELETELINE
        commit("plot_data", result);
      });
    },
  },

  modules: {
    settings,
  },
});
