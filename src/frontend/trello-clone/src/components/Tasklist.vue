<template>
    <div>
        <div class="tile is-child box">
            <h2>Tasklist here - {{tasklistId}}</h2>
        </div>
    </div>
</template>

<script>
export default {

  data() {
    return {
      
    };
  },

  props:[
      'tasklistId',
  ],

  components :{
    },

  methods : {
  },


  computed : {
  }, // End of computed

};
</script>

<style scoped>

</style>