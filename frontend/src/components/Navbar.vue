<template>
  <nav class="navbar bg-body-tertiary">
    <div class="container-fluid">
      <a class="navbar-brand">Games Gustavin</a>
      <NavSearch />
    </div>
  </nav>
</template>

<script>
import NavSearch from "@/components/buttons/NavSearch.vue";
export default {
  name: "NavBar",
  props: {
    msg: String,
  },
  components: {
    NavSearch,
  },
};
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
