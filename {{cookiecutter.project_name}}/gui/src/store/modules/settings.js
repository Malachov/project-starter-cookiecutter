// Do not put everything into index.js, that would be a mess and name collisions would appear.
// If there are variables (or methods) that are in close relation, put it into module
// If you use for example settings module, you that need to specify module if acessing it. Check develop.vue for how to use this module example

import { getField, updateField } from "vuex-map-fields";

const state = () => ({
  settings_one: {
    one: "nice",
    two: 2,
  },

  delayed: 10,
});

const getters = {
  getField,
};

const mutations = {
  updateField,
  update_settings_one(state, { val }) {
    state.settings_one = val;
  },
  update_settings_two(state, { val }) {
    state.settings_two = val;
  },
};

export default {
  namespaced: true,
  state,
  getters,
  mutations,
};
