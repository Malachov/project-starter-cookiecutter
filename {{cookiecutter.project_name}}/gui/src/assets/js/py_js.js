import store from "@/store";

export function mutate(property, value) {
  store.commit("shared/mutate", [property, value]);
}

export function create_alert(caption, message, error = "", type = "info") {
  store.commit("alert", {
    caption: caption,
    message: message,
    error: error,
    type: type,
  });
}
