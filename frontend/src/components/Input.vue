<template>
  <!-- <v-layout  align-center row justify-center>  -->
  <v-layout align-start justify-center row>
    <v-card color="gray" dark max-height="250px" max-width="500">
      <v-card-title class="headline gray lighten-3">Procure sua musica favorita</v-card-title>
      <v-card-text>Explore milhares de musicas e escolha qual vocabulario gostaria de aprender.</v-card-text>
      <v-card-text>
        <v-text-field
          flat
          solo-inverted
          hide-details
          prepend-inner-icon="search"
          label="Search"
          class
          v-model="song"
          v-on:keyup="search(7)"
          v-on:keyup.enter="search(4)"
        ></v-text-field>
      </v-card-text>
      <v-divider color="white"></v-divider>
      <v-expand-transition>
        <v-list
          class="gray lighten-3"
          v-scroll:#scroll-target
          style="overflow:scroll; height:250px;"
          v-if="song"
        >
          <v-list-tile v-for="(resul,i) in result" :key="i">
            <v-list-tile-content v-on:click="lyrics(resul.Music, resul.Artist)">
              <v-list-tile-title v-text="resul.Music"></v-list-tile-title>
              <v-list-tile-sub-title v-text="resul.Artist"></v-list-tile-sub-title>
              <v-divider color="white"></v-divider>
            </v-list-tile-content>
          </v-list-tile>
        </v-list>
      </v-expand-transition>
    </v-card>
  </v-layout>
</template>


<script>
const axios = require("axios");
export default {
  data: () => ({
    result: null,
    song: null,
    Artist: null,
    Music: null,
    vocabulary: null,
    song_lyric: null
  }),

  methods: {
    search(n_char) {
      if (this.song.length >= n_char) {
        axios
          .get("/search_song?song=" + this.song)
          .then(response => (this.result = response.data.results));
      }
    },
    lyrics(Music, Artist) {
      axios
        .get("/lyric?art=" + Artist + "&music=" + Music)
        .then(
          response => (
            (this.song_lyric = response.data.lyric),
            (this.vocabulary = response.data.vocabulary),
             this.$router.push({
              name: "Lyric",
              params: { lyri: this.song_lyric, vocabulary : this.vocabulary }
            })
          )
        );
    }
  }
};
</script>

