<template>
  <Navbar />
  <div>
    <GameCard />
  </div>
</template>

<script>
// @ is an alias to /src
import Navbar from "@/components/Navbar.vue";
import GameCard from "@/components/CardHome.vue";

export default {
  name: "HomeView",
  components: {
    Navbar,
    GameCard,
  },
  data() {
    return {
      data: "",
    };
  },
  created() {},
};
</script>
