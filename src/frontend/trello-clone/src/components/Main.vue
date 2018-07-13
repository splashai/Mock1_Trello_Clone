<template>
  <div class="container">
    
    <div class="container">
      <div class="notification">
        <span class="icon has-text-info">
        <i class="fas fa-user"></i>
        </span></i><span><strong>Personal Boards</strong></span>
      </div>
    </div>

    <div class="tile is-ancestor">
        <div class="tile is-parent">
            <div class="tile is-child box" v-for="(board, index) in boards"  @click="cardClicked(board.url)">
                <p class="title"  >{{board.name}}</p>
                <p>{{board.description}}</p>
                <p>Created Date : {{board.create_date.slice(0,10) }}</p>
            </div>
        </div>
    </div>

  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      boards: [],
      errors: []
    };
  },

  methods : {

    cardClicked : function (boardUrl){
      console.log(boardUrl);
    },


  },

  // Fetches posts when the component is created.
  created() {
    axios
      .get(`http://127.0.0.1:8000/api/v1/boards/`)
      .then(response => {
        this.boards = response.data;
      })
      .catch(e => {
        this.errors.push(e);
      });
  }
};
</script>