<template>
  <div class="container">
    <div class="wrap" v-for="card in cards" :key="card.id">
      <div
        class="box"
        :style="`background-image: url(${card.photo})`"
        v-on:click="say(card.id, card.title)"
      >
        <div class="date">
          <h3 v-if="card.metacritic">MetaCritic: {{ card.metacritic }}</h3>
        </div>
        <h1>{{ card.title }}</h1>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "GameCard",
  props: {
    msg: String,
  },
  components: {},
  computed: {
    backgroundImage() {
      return `background-image: url("https://media.rawg.io/media/games/4ea/4ea507ceebeabb43edbc09468f5aaac6.jpg}")`;
    },
  },
  data() {
    return {
      cards: [],
    };
  },
  mounted() {
    this.fetchCards();
  },
  methods: {
    fetchCards() {
      axios
        .get("http://localhost:8000")
        .then((response) => {
          this.cards = response.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
body {
  font-family: "Roboto", sans-serif;
  background: #fff;
}

.container {
  width: 100%;
  height: 500px;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-evenly;
}
.wrap {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-wrap: wrap;
  flex-wrap: wrap;
  -webkit-box-pack: center;
  -ms-flex-pack: center;
  justify-content: center;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
  -webkit-box-orient: horizontal;
  -webkit-box-direction: normal;
  -ms-flex-direction: row;
  flex-direction: row;
}

.box {
  margin: 10px;
  width: 300px;
  height: 490px;
  text-align: center;
  border-radius: 3px;
  -webkit-transition: 200ms ease-in-out;
  -o-transition: 200ms ease-in-out;
  transition: 200ms ease-in-out;
  -webkit-box-shadow: 0 0 15px rgba(0, 0, 0, 0.3);
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.3);
}
.box:hover {
  margin-bottom: -10px;
  -webkit-box-shadow: 0 0 5px rgba(0, 0, 0, 0.7);
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.7);
}
.box h1 {
  color: #fff;
  padding: 30px;
  margin-top: 100px;
  text-align: center;
  font-weight: 100;
  font-size: 25px;
  background: rgba(0, 0, 0, 0.8);
  -webkit-box-shadow: 0 0 30px rgba(0, 0, 0, 0.7);
  box-shadow: 0 0 30px rgba(0, 0, 0, 0.8);
}

.date h4 {
  color: #fff;
  font-weight: 300;
  text-align: center;
  letter-spacing: 3px;
  text-shadow: 0 0 3px rgba(0, 0, 0, 0.9);
}
.poster {
  width: 130px;
  height: 130px;
  margin: 120px auto;
  position: relative;
  border-radius: 100px;
}
.poster h4 {
  top: 16px;
  color: #fff;
  position: relative;
  font-size: 80px;
  text-align: center;
  font-weight: 100;
}
.box {
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
}

h3 {
  color: #fff;
  font-weight: 300;
  text-align: center;
  letter-spacing: 3px;
  text-shadow: 0 0 3px rgba(0, 0, 0, 0.9);
}

/* POSTER*/
.poster {
  background: #2b5876; /* fallback for old browsers */
  background: -webkit-linear-gradient(
    to right,
    #4e4376,
    #2b5876
  ); /* Chrome 10-25, Safari 5.1-6 */
  background: -webkit-gradient(
    linear,
    left top,
    right top,
    from(#4e4376),
    to(#2b5876)
  );
  background: -webkit-linear-gradient(left, #4e4376, #2b5876);
  background: -o-linear-gradient(left, #4e4376, #2b5876);
  background: linear-gradient(
    to right,
    #4e4376,
    #2b5876
  ); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
  -webkit-box-shadow: 0 0 20px darkblue;
  box-shadow: 0 0 20px darkblue;
}
/*  FOLLOW*/
.Follow {
  background: url("https://pbs.twimg.com/profile_images/959092900708544512/v4Db9QRv_bigger.jpg")
    no-repeat center / contain;
  width: 50px;
  height: 50px;
  bottom: 9px;
  right: 20px;
  display: block;
  position: fixed;
  border-radius: 50%;
  z-index: 999;
  animation: rotation 10s infinite linear;
}

@-webkit-keyframes rotation {
  from {
    -webkit-transform: rotate(0deg);
  }
  to {
    -webkit-transform: rotate(359deg);
  }
}
</style>
