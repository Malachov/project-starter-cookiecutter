{% raw -%}
<template>
  <div v-if="alert.show">
    <v-row justify="center">
      <v-col cols="10">
        <v-alert prominent dense outlined :type="alert.type" class="my-pre-wrapped pa-4">
          <v-row align="center">
            <v-col class="grow">
              <h2>{{ alert.caption }}</h2>
              {{ alert.message }}
              <br v-if="alert.message" />
              <br v-if="alert.message" />
              <p class="my-pre-wrapped">{{ alert.error }}</p>
            </v-col>
            <v-col class="shrink ma-4">
              <v-btn icon color="red darken-1" class="mr-8" @click="reset_alert">
                <v-icon size="80">mdi-close</v-icon>
              </v-btn>
            </v-col>
          </v-row>
        </v-alert>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import { mapFields } from "vuex-map-fields";

export default {
  computed: {
    ...mapFields(["alert"]),
  },

  methods: {
    reset_alert: function () {
      this.alert = {
        show: false,
        caption: "",
        message: "",
        error: "",
        type: "",
      };
    },
  },
};
</script>

<style>
.v-alert__content {
  margin-left: 25px !important;
}

.v-alert__icon {
  margin-left: 30px !important;
}
</style>
{%- endraw %}
