<template>
  <div class="container mt-5">
    <h2>Subscription Languages</h2>
    <nav aria-label="breadcrumb">
      <ol class="breadcrumb">
        <li class="breadcrumb-item"><router-link to="/">Home</router-link></li>
        <li class="breadcrumb-item active" aria-current="page">Subscription Languages</li>
      </ol>
    </nav>

    <table class="table table-striped mt-4">
      <thead>
        <tr>
          <th>Name</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-if="addingNew">
          <td><input type="text" v-model="newSubscriptionLanguage.name" class="form-control" /></td>
          <td>
            <button class="btn btn-primary btn-sm" @click="saveNewSubscriptionLanguage">Save</button>
            <button class="btn btn-secondary btn-sm" @click="cancelNewSubscriptionLanguage">Cancel</button>
          </td>
        </tr>
        <tr v-for="language in subscriptionLanguages" :key="language._id">
          <template v-if="editMode === language._id">
            <td><input type="text" v-model="editSubscriptionLanguage.name" class="form-control" /></td>
            <td>
              <button class="btn btn-primary btn-sm" @click="updateSubscriptionLanguage(language._id)">Save</button>
              <button class="btn btn-secondary btn-sm" @click="cancelEdit">Cancel</button>
            </td>
          </template>
          <template v-else>
            <td>{{ language.name }}</td>
            <td>
              <button class="btn btn-warning btn-sm" @click="editSubscriptionLanguageFunc(language)">Edit</button>
              <button class="btn btn-danger btn-sm" @click="showDeleteModal(language._id)">Delete</button>
            </td>
          </template>
        </tr>
      </tbody>
    </table>
    <button class="btn btn-success mt-3" @click="startAddingNew">Add New Language</button>

    <confirmation-modal
      v-if="showConfirmationModal"
      :show="showConfirmationModal"
      title="Confirm Delete"
      message="Are you sure you want to delete this subscription language?"
      @close="hideDeleteModal"
      @confirm="deleteSubscriptionLanguage"
    />
  </div>
</template>

<script>
import subscriptionLanguageService from '../services/subscriptionLanguageService';
import ConfirmationModal from './ConfirmationModal.vue';

export default {
  components: {
    ConfirmationModal
  },
  data() {
    return {
      subscriptionLanguages: [],
      addingNew: false,
      editMode: null,
      showConfirmationModal: false,
      languageToDelete: null,
      newSubscriptionLanguage: {
        name: ''
      },
      editSubscriptionLanguage: {
        name: ''
      }
    };
  },
  created() {
    this.loadSubscriptionLanguages();
  },
  methods: {
    loadSubscriptionLanguages() {
      subscriptionLanguageService.getSubscriptionLanguages().then(response => {
        this.subscriptionLanguages = response.data;
      }).catch(error => {
        console.error("There was an error retrieving the subscription languages!", error);
      });
    },
    startAddingNew() {
      this.addingNew = true;
      this.resetNewSubscriptionLanguage();
    },
    cancelNewSubscriptionLanguage() {
      this.addingNew = false;
    },
    resetNewSubscriptionLanguage() {
      this.newSubscriptionLanguage = {
        name: ''
      };
    },
    saveNewSubscriptionLanguage() {
      subscriptionLanguageService.createSubscriptionLanguage(this.newSubscriptionLanguage).then(() => {
        this.loadSubscriptionLanguages();
        this.addingNew = false;
      }).catch(error => {
        console.error("There was an error saving the subscription language!", error);
      });
    },
    editSubscriptionLanguageFunc(language) {
      this.editMode = language._id;
      this.editSubscriptionLanguage = { ...language };
    },
    cancelEdit() {
      this.editMode = null;
    },
    updateSubscriptionLanguage(id) {
      subscriptionLanguageService.updateSubscriptionLanguage(id, this.editSubscriptionLanguage).then(() => {
        this.loadSubscriptionLanguages();
        this.editMode = null;
      }).catch(error => {
        console.error("There was an error updating the subscription language!", error);
      });
    },
    showDeleteModal(id) {
      this.languageToDelete = id;
      this.showConfirmationModal = true;
    },
    hideDeleteModal() {
      this.showConfirmationModal = false;
      this.languageToDelete = null;
    },
    deleteSubscriptionLanguage() {
      subscriptionLanguageService.deleteSubscriptionLanguage(this.languageToDelete).then(() => {
        this.loadSubscriptionLanguages();
        this.hideDeleteModal();
      }).catch(error => {
        console.error("There was an error deleting the subscription language!", error);
      });
    }
  }
};
</script>

<style scoped>
/* Add your styles here */
</style>
