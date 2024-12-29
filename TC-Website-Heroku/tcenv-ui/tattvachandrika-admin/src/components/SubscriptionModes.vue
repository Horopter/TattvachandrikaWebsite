<template>
  <div class="container mt-5">
    <h2>Subscription Modes</h2>
    <nav aria-label="breadcrumb">
      <ol class="breadcrumb">
        <li class="breadcrumb-item"><router-link to="/">Home</router-link></li>
        <li class="breadcrumb-item active" aria-current="page">Subscription Modes</li>
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
          <td><input type="text" v-model="newSubscriptionMode.name" class="form-control" /></td>
          <td>
            <button class="btn btn-primary btn-sm" @click="saveNewSubscriptionMode">Save</button>
            <button class="btn btn-secondary btn-sm" @click="cancelNewSubscriptionMode">Cancel</button>
          </td>
        </tr>
        <tr v-for="mode in subscriptionModes" :key="mode._id">
          <template v-if="editMode === mode._id">
            <td><input type="text" v-model="editSubscriptionMode.name" class="form-control" /></td>
            <td>
              <button class="btn btn-primary btn-sm" @click="updateSubscriptionMode(mode._id)">Save</button>
              <button class="btn btn-secondary btn-sm" @click="cancelEdit">Cancel</button>
            </td>
          </template>
          <template v-else>
            <td>{{ mode.name }}</td>
            <td>
              <button class="btn btn-warning btn-sm" @click="editSubscriptionModeFunc(mode)">Edit</button>
              <button class="btn btn-danger btn-sm" @click="showDeleteModal(mode._id)">Delete</button>
            </td>
          </template>
        </tr>
      </tbody>
    </table>
    <button class="btn btn-success mt-3" @click="startAddingNew">Add New Mode</button>

    <confirmation-modal
      v-if="showConfirmationModal"
      :show="showConfirmationModal"
      title="Confirm Delete"
      message="Are you sure you want to delete this subscription mode?"
      @close="hideDeleteModal"
      @confirm="deleteSubscriptionMode"
    />
  </div>
</template>

<script>
import subscriptionModeService from '../services/subscriptionModeService';
import ConfirmationModal from './ConfirmationModal.vue';

export default {
  components: {
    ConfirmationModal
  },
  data() {
    return {
      subscriptionModes: [],
      addingNew: false,
      editMode: null,
      showConfirmationModal: false,
      modeToDelete: null,
      newSubscriptionMode: {
        name: ''
      },
      editSubscriptionMode: {
        name: ''
      }
    };
  },
  created() {
    this.loadSubscriptionModes();
  },
  methods: {
    loadSubscriptionModes() {
      subscriptionModeService.getSubscriptionModes().then(response => {
        this.subscriptionModes = response.data;
      }).catch(error => {
        console.error("There was an error retrieving the subscription modes!", error);
      });
    },
    startAddingNew() {
      this.addingNew = true;
      this.resetNewSubscriptionMode();
    },
    cancelNewSubscriptionMode() {
      this.addingNew = false;
    },
    resetNewSubscriptionMode() {
      this.newSubscriptionMode = {
        name: ''
      };
    },
    saveNewSubscriptionMode() {
      subscriptionModeService.createSubscriptionMode(this.newSubscriptionMode).then(() => {
        this.loadSubscriptionModes();
        this.addingNew = false;
      }).catch(error => {
        console.error("There was an error saving the subscription mode!", error);
      });
    },
    editSubscriptionModeFunc(mode) {
      this.editMode = mode._id;
      this.editSubscriptionMode = { ...mode };
    },
    cancelEdit() {
      this.editMode = null;
    },
    updateSubscriptionMode(id) {
      subscriptionModeService.updateSubscriptionMode(id, this.editSubscriptionMode).then(() => {
        this.loadSubscriptionModes();
        this.editMode = null;
      }).catch(error => {
        console.error("There was an error updating the subscription mode!", error);
      });
    },
    showDeleteModal(id) {
      this.modeToDelete = id;
      this.showConfirmationModal = true;
    },
    hideDeleteModal() {
      this.showConfirmationModal = false;
      this.modeToDelete = null;
    },
    deleteSubscriptionMode() {
      subscriptionModeService.deleteSubscriptionMode(this.modeToDelete).then(() => {
        this.loadSubscriptionModes();
        this.hideDeleteModal();
      }).catch(error => {
        console.error("There was an error deleting the subscription mode!", error);
      });
    }
  }
};
</script>

<style scoped>
/* Add your styles here */
</style>
