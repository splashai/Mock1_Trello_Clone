<template>
  <div>
      <ul v-if="boards && boards.length">
        <li v-for="(board, index) in boards">
        <p><strong>{{board.name}}</strong></p>
      <p>{{board.url}}</p>
    </li>
  </ul>

  <!-- <ul v-if="errors && errors.length">
    <li v-for="error in errors">
      {{error.message}}
    </li>
  </ul> -->
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