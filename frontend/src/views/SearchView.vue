<template>
  <Navbar />
  <div>
    <GameCard />
  </div>
</template>

<script>
// @ is an alias to /src
import Navbar from "@/components/Navbar.vue";
import GameCard from "@/components/Card.vue";

export default {
  name: "SearchView",
  components: {
    Navbar,
    GameCard,
  },
  data() {
    return {
      data: "",
    };
  },
};
</script>
