{% raw -%}
<template>
  <v-dialog v-model="dialog" max-width="80%">
    <template v-slot:activator="{ on, attrs }">
      <v-btn
        icon
        slot="activator"
        class="ma-4"
        :color="color_settings"
        @mouseover="color_settings = 'blue lighten-2'"
        @mouseleave="color_settings = ''"
        v-bind="attrs"
        v-on="on"
      >
        <v-icon size="50">mdi-cog</v-icon>
      </v-btn>
    </template>

    <v-card min-height="90vh" class="pa-16">
      <v-toolbar flat height="100px" color="transparent">
        <v-spacer></v-spacer>
        <v-btn icon class="ma-4" color="red darken-1" @click="dialog = false">
          <v-icon size="70">mdi-close</v-icon>
        </v-btn>
      </v-toolbar>

      <v-col cols="10">
        <v-tabs v-model="tab" vertical>
          <h1 class="black--text mb-4">User settings</h1>
          <v-tab> Settings tab 1 </v-tab>

          <v-tab> Settings tab 2 </v-tab>

          <v-tab-item transition="false">
            <div class="my-flex-column">
              <FormulateForm v-model="local_settings_one" :schema="schema_one" />
            </div>
          </v-tab-item>

          <v-tab-item transition="false">
            <div class="my-flex-column">
              <FormulateInput
                label="Normal"
                type="range"
                min="0"
                max="100"
                v-model="range_normal"
                show-value="true"
              />
              <p>{{ range_normal }}</p>
              <FormulateInput
                label="Lazy load - delayed"
                type="range"
                name="range"
                min="0"
                max="100"
                value="45"
                v-model="delayed_call"
                show-value="true"
              />
              <p>{{ delayed }}</p>
            </div>
          </v-tab-item>
        </v-tabs>
      </v-col>
    </v-card>
  </v-dialog>
</template>

<script>
import { mapFields } from "vuex-map-fields";
import { isEqual } from "lodash";

export default {
  data: () => ({
    tab: 0,
    dialog: false,
    color_settings: "",

    local_settings_one: {},

    last_settings: null,
    delayed_local: null,
    range_normal: 10,

    schema_one: [
      {
        component: "h3",
        children: "Main settings",
      },
      {
        label: "One",
        name: "one",
        type: "select",
        options: {
          nice: "Nice",
          nasty: "Nasty",
        },
      },
      {
        component: "h3",
        children: "Display",
      },
      {
        label: "String settings",
        name: "string_settings",
        type: "text",
      },
    ],
  }),

  computed: {
    ...mapFields("settings", ["delayed"]),

    // This values will be editted immediately after changing value
    delayed_call: {
      get() {
        return this.delayed_local;
      },
      set(value) {
        this.delayed_local = value;
        this.last_settings = value;
        setTimeout(() => {
          if (
            value == this.last_settings && // User is not changing value anymore
            !isEqual(this.delayed, value) // It change'd back again
            // Add some another conditions like - if not still in processing
          ) {
            this.delayed = value;
          }
        }, 1000);
      },
    },
  },

  watch: {
    dialog(value) {
      if (value) {
        this.pull_settings();
      }
      if (!value) {
        this.push_settings();
      }
    },
  },

  methods: {
    // This values will be updated at once after closing dialog
    push_settings() {
      this.$store.commit("settings/update_settings_one", { val: this.local_settings_one });
    },

    pull_settings() {
      this.local_settings_one = this.$store.state.settings.settings_one;
      this.delayed_local = this.$store.state.settings.delayed;
    },
  },
};
</script>

<style>
.v-tabs-bar__content {
  align-items: flex-start;
}
</style>
{%- endraw %}
