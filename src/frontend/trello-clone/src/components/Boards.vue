<template>
  <div>
    
    <div class="container">
      <div class="notification">
        <span class="icon has-text-info">
        <i class="fas fa-user"></i>
        </span><span><strong>Personal Boards</strong></span>
      </div>
    </div>

    <div class="tile is-ancestor">
        <div class="tile is-parent">
            <div class="tile is-child box" v-for="board in getBoards"  @click="cardClicked(board.url)">
                <p class="title"  >{{board.name}}</p>
                <p>{{board.description}}</p>
                <p>Created Date : {{board.create_date.slice(0,10) }}</p>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapMutations, mapActions } from 'vuex'

export default {
  data() {
    return {
      errors: []
    };
  },

  methods : {

    cardClicked : function (boardUrl){
      this.$store.dispatch('getBoardDetailsAPI', {
        url : boardUrl,
      });
    },

  },


  computed : {

    ...mapGetters([
      'getBoards',
    ]),

    ...mapMutations([
      'getBoardsAPI',
    ]),

    ...mapActions([
      'getBoardDetailsAPI'
    ]),
    

  },

  // Fetches posts when the component is created.
  created() {
    this.$store.commit('getBoardsAPI');
  }
};
</script>