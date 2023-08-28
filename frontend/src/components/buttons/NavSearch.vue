<template>
  <form class="d-flex" role="search" @submit="sendForm($event)">
    <input
      class="form-control me-2"
      type="text"
      v-model="gameName"
      placeholder="Gimme a game name"
      aria-label="Search"
    />
    <button class="btn btn-outline-success" type="submit" href="searchResult">
      Search
    </button>
  </form>
</template>

<script>
import VueCookies from "vue-cookies";
export default {
  name: "NavSearch",
  props: {
    msg: String,
  },
  data() {
    return {
      gameName: "",
    };
  },
  methods: {
    sendForm(e) {
      e.preventDefault();
      let gameName = this.gameName;
      VueCookies.set("dataR", gameName);
      this.$router.push({ path: "/" });
    },
  },
};
</script>
