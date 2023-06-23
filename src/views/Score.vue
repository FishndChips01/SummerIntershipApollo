<script>
import axios from 'axios';
import APIRequest from '../components/APIRequest.vue';

export default {
  components: {
    APIRequest
  },
  data() {
    return {
      users: []
    };
  },
  mounted() {
    this.fetchUsers();
  },
  methods: {
    fetchUsers() {
      axios.get('http://localhost:3001/comment')
        .then(response => {
          this.users = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>


<template>
  <div>
    <a href="/comment">
      <button class= "Comment-button">Enter your comment here</button>
    </a>

    <div class="content">
      <table>
        <tr>
          <th>Ranking</th>
          <th>User Name</th>
          <th>Score</th>
        </tr>
        <tr v-for="user in users" :key="user.id">
          <td>{{ user.user_rank }}</td>
          <td>{{ user.username }}</td>
          <td>{{ user.score }}</td>
        </tr>
      </table>
    </div>
  </div>
</template>


<style> 
body {
  background-color: royalblue ;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

h1 {
  text-align: center;
  margin-top: 20px;
  color: black;
}

th,
td {
  padding: 12px;
  text-align: left;
  border-bottom: 1px solid wheat;
}

th {
  background-color: grey;
  color: black;
}


tr:nth-child(even) {
  background-color: plum;
  color: black;
}


tr.highlight:nth-child(even) {
  background-color: gold; 
}

tr:hover {
  background-color: dimgray;
}

td:first-child {
  font-weight: bold;
}

.comment-button {
  display: block;
  margin: 20px auto;
  padding: 15px 30px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 18px;
  transition: background-color 0.3s ease;
}

.comment-button:hover {
  background-color: #0056b3;
}
</style>