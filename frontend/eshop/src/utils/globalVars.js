import Vue from "vue";

export const globalVars = new Vue({
  data: {
    apiBaseUrl: process.env.VUE_APP_API_BASE_URL
  }
});
