<template>
    <div>
        <div class="tile is-child box">
            <h2>{{local_tasklist.name}}</h2>
            <div v-for="(card, index) in local_tasklist.card_set" :key="index">
                <div class="card">
                    <div class="media-content">
                        <p class="title is-6">{{card.title}}</p>
                    </div>
                    <div class="content">
                        <p>{{card.description}}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
// import { mapGetters } from 'vuex';

export default {

  data() {
    return {

    };
  },

  props:[
      'tasklistId',
  ],

  computed :{
      local_tasklist : function(){
        //   return '1';
          return this.$store.getters.getTasklistDetails(this.tasklistId);
      },
    },

  methods : {
  },

};
</script>

<style scoped>
h2{
    text-decoration: underline;
}
.card{
    margin : 10px 0px;
}
</style>