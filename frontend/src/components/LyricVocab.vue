<template>
 <v-app id="inspire">
    <v-navigation-drawer v-model="drawer" fixed app>
      <v-list dense>
        <v-list-tile @click="gotTo('')">
          <v-list-tile-action>
            <v-icon>home</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Home</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <v-list-tile @click="gotTo('Login')">
          <v-list-tile-action>
            <v-icon>account_box</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Login</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>
    <v-toolbar color="black" dark fixed app>
      <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
      <v-toolbar-title>YourWords</v-toolbar-title>
    </v-toolbar>
   <v-content style="background:white">
      <v-flex >
      <!-- <v-layout align-start justify-start row fill-height> -->
      <v-card >
          <div>
            <div v-html="this.lyri">
             </div>
          </div>
        </v-card>
         </v-flex>
       <!-- </v-layout> -->
       <!-- <v-layout align-start justify-end row fill-height> -->
         <v-flex >
         <v-card>
          <div>
            <div v-html="this.vocabulary">
             </div>
          </div>
        </v-card>
        </v-flex>
       <!-- </v-layout> -->
   </v-content>
     <v-footer color="black" app>
      <span class="white--text">&copy; 2019 JackCodeCoffe</span>
    </v-footer>
  </v-app>
</template>

<script>
  export default {
    data: () => ({
    drawer: false
  }),
  props: {
    source: String,
    lyri : String,
    vocabulary : String
  },
  //   props : ["lyri","vocabulary"],
      
  }
  
</script>