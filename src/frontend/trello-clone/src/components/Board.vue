<template>
<div>
    <div class="container">
        <nav class="level">
        <!-- Left side -->
        <div class="level-left">
            <div class="level-item">
            <p class="subtitle is-5">
                <strong>{{getBoardDetails.name}}</strong> - {{getBoardDetails.description}}
            </p>
            </div>
        </div>

        <!-- Right side -->
        <div class="level-right">
            <p class="level-item">You have {{getBoardDetails.tasklist_set.length}} tasklist in this board.</p>
        </div>
        </nav>

        <div class="container">
            <div class="tile is-ancestor">
                <div v-for="(tasklist, index) in getBoardDetails.tasklist_set" :key="index">
                    <app-tasklist v-bind:tasklistId="tasklist.id"></app-tasklist>
                </div>
            </div>
        </div>
    
    </div>  <!-- End of container -->

</div>
</template>

<script>
import { mapGetters } from 'vuex'
import Tasklist from './Tasklist'

export default {
  data() {
    return {
      
    };
  },

  components :{
      'app-tasklist' : Tasklist,
    },

  methods : {

    
  },


  computed : {

    ...mapGetters([
      'getBoardDetails',
    ]),

    

  }, // End of computed

};

</script>


<style scoped>
    .container {
        margin : 20px 0px;
        border : 1px solid #eee;
    }
    .level{
        margin : 20px 0px;
        border : 1px solid #eee;
    }
    .tile{
        padding : 20px;
    }
    
</style>