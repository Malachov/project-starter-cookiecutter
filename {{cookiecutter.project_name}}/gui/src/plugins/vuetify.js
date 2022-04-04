import Vue from "vue";
import Vuetify from "vuetify/lib";

Vue.use(Vuetify);

const opts = {
  theme: {
    themes: {
      light: {
        //
      },
    },
  },
  icons: {
    iconfont: "mdi",
  },
};

export default new Vuetify(opts);
