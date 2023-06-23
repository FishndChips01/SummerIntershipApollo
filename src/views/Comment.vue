<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      comment: ''
    };
  },
  methods: {
    submitComment() {
      const commentData = {
        username: this.username,
        comment: this.comment
      };


      // This sends the data to the server
      axios.post('/api/comments', commentData)
        .then(response => {
          console.log(response.data);
          alert('Comment submitted!');

          // This clears the input fields 
          this.username = '';
          this.comment = '';
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>


<template>
   <div id="app"></div>
  <div class="background">
    <div>
      <div class="container">
        <div class="link">
          <a href="/score">
            <button class="scoreboard-button">Check the ScoreBoard Here</button>
          </a>
        </div>
      </div>

      <div class="picture">
        <img src="https://cdn.discordapp.com/attachments/758287762641387551/1118967731761455215/My_project.png" class="logo">
      </div>

      <div class="box">
        <h2 class="box-title">Type your comments here</h2>
        
        <div>
          <input type="text" v-model="username" placeholder="Username">
          <textarea v-model="comment" placeholder="Enter your comment"></textarea>
          <button @click="submitComment">Submit</button>
        </div>
      </div>
    </div>
  </div>

</template>



<style>

.background {
  background-color: #007bff;
}

.box {
  width: 400px;
  margin: 20px auto;
  padding: 20px;
  background-color: #f2f2f2;
  border-radius: 5px;
}

.box-title {
  text-align: center;
  margin-top: 0;
  color: #333;
}

.box input[type="text"],
.box textarea {
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 3px;
  resize: vertical;
}

.box button {
  display: block;
  width: 100%;
  padding: 10px;
  background-color: #4caf50;
  color: #fff;
  border: none;
  border-radius: 3px;
  cursor: pointer;
}

.box button:hover {
  background-color: #45a049;
}

.container {
  text-align: center;
}

.link {
  margin-top: 20px;
}

.scoreboard-button {
  padding: 10px 20px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 3px;
  cursor: pointer;
}

.picture {
  text-align: center;
  margin-top: 20px;
}

.logo {
  width: 200px;
  height: auto;
}
</style>