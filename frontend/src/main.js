import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import "bootstrap/dist/css/bootstrap.css";
import bootstrap from "bootstrap/dist/js/bootstrap.js";
import axios from "axios";
import VueAxios from "vue-axios";

createApp(App).use(router).use(bootstrap).use(VueAxios, axios).mount("#app");
