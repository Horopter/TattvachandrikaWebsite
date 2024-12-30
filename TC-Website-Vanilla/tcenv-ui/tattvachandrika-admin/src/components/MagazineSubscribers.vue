<template>
  <div class="container mt-5">
    <nav aria-label="breadcrumb">
      <ol class="breadcrumb">
        <li class="breadcrumb-item"><router-link to="/">Home</router-link></li>
        <li class="breadcrumb-item active" aria-current="page">Magazine Subscribers</li>
      </ol>
    </nav>
    <h2>Magazine Subscribers</h2>
    <button class="btn btn-primary mb-3" @click="openAddSubscriberModal">Add Subscriber</button>

    <!-- Tabs for Active and Inactive Subscribers -->
    <ul class="nav nav-tabs" id="myTab" role="tablist">
      <li class="nav-item" role="presentation">
        <button class="nav-link active" id="active-tab" data-bs-toggle="tab" data-bs-target="#active" type="button" role="tab" aria-controls="active" aria-selected="true">Active Subscribers</button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link" id="inactive-tab" data-bs-toggle="tab" data-bs-target="#inactive" type="button" role="tab" aria-controls="inactive" aria-selected="false">Inactive Subscribers</button>
      </li>
    </ul>
    <div class="tab-content" id="myTabContent">
      <!-- Active Subscribers Tab -->
      <div class="tab-pane fade show active" id="active" role="tabpanel" aria-labelledby="active-tab">
        <!-- Nested Tabs for Current Subscribers and Waiting for Renewal -->
        <ul class="nav nav-tabs mt-3" id="activeSubTab" role="tablist">
          <li class="nav-item" role="presentation">
            <button class="nav-link active" id="current-tab" data-bs-toggle="tab" data-bs-target="#current" type="button" role="tab" aria-controls="current" aria-selected="true">Current Subscribers</button>
          </li>
          <li class="nav-item" role="presentation">
            <button class="nav-link" id="renewal-tab" data-bs-toggle="tab" data-bs-target="#renewal" type="button" role="tab" aria-controls="renewal" aria-selected="false">Waiting for Renewal</button>
          </li>
        </ul>
        <div class="tab-content" id="activeSubTabContent">
          <div class="tab-pane fade show active" id="current" role="tabpanel" aria-labelledby="current-tab">
            <table class="table table-striped mt-3">
              <thead>
                <tr>
                  <th>Name</th>
                  <th>Registration Number</th>
                  <th>City/Town</th>
                  <th>State</th>
                  <th>Phone</th>
                  <th>Email</th>
                  <th>Actions</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="subscriber in currentSubscribers" :key="subscriber._id">
                  <td>{{ subscriber.name }}</td>
                  <td>{{ subscriber.registration_number }}</td>
                  <td>{{ subscriber.city_town }}</td>
                  <td>{{ subscriber.state }}</td>
                  <td>{{ subscriber.phone }}</td>
                  <td>{{ subscriber.email }}</td>
                  <td>
                    <button class="btn btn-primary btn-sm" @click="viewSubscriber(subscriber._id)">View</button>
                    <button class="btn btn-secondary btn-sm" @click="openEditSubscriberModal(subscriber)">Edit</button>
                    <button class="btn btn-danger btn-sm" @click="confirmDeleteSubscriber(subscriber._id)">Delete</button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
          <div class="tab-pane fade" id="renewal" role="tabpanel" aria-labelledby="renewal-tab">
            <table class="table table-striped mt-3">
              <thead>
                <tr>
                  <th>Name</th>
                  <th>Registration Number</th>
                  <th>City/Town</th>
                  <th>State</th>
                  <th>Phone</th>
                  <th>Email</th>
                  <th>Actions</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="subscriber in waitingForRenewalSubscribers" :key="subscriber._id">
                  <td>{{ subscriber.name }}</td>
                  <td>{{ subscriber.registration_number }}</td>
                  <td>{{ subscriber.city_town }}</td>
                  <td>{{ subscriber.state }}</td>
                  <td>{{ subscriber.phone }}</td>
                  <td>{{ subscriber.email }}</td>
                  <td>
                    <button class="btn btn-primary btn-sm" @click="viewSubscriber(subscriber._id)">View</button>
                    <button class="btn btn-secondary btn-sm" @click="openEditSubscriberModal(subscriber)">Edit</button>
                    <button class="btn btn-danger btn-sm" @click="confirmDeleteSubscriber(subscriber._id)">Delete</button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
      
      <!-- Inactive Subscribers Tab -->
      <div class="tab-pane fade" id="inactive" role="tabpanel" aria-labelledby="inactive-tab">
        <table class="table table-striped mt-3">
          <thead>
            <tr>
              <th>Name</th>
              <th>Registration Number</th>
              <th>City/Town</th>
              <th>State</th>
              <th>Phone</th>
              <th>Email</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="subscriber in inactiveSubscribers" :key="subscriber._id">
              <td>{{ subscriber.name }}</td>
              <td>{{ subscriber.registration_number }}</td>
              <td>{{ subscriber.city_town }}</td>
              <td>{{ subscriber.state }}</td>
              <td>{{ subscriber.phone }}</td>
              <td>{{ subscriber.email }}</td>
              <td>
                <button class="btn btn-primary btn-sm" @click="viewSubscriber(subscriber._id)">View</button>
                <button class="btn btn-secondary btn-sm" @click="openEditSubscriberModal(subscriber)">Edit</button>
                <button class="btn btn-success btn-sm" @click="activateSubscriber(subscriber._id)">Activate</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Add/Edit Subscriber Modal -->
    <add-edit-subscriber-modal 
      :show="showAddEditSubscriberModal" 
      :subscriber="selectedSubscriber" 
      :categories="categories" 
      :types="types" 
      @close="closeAddEditSubscriberModal" 
      @save="saveSubscriber">
    </add-edit-subscriber-modal>

    <!-- Confirmation Modal -->
    <confirmation-modal
      v-if="showConfirmationModal"
      :show="showConfirmationModal"
      title="Confirm Delete"
      message="Are you sure you want to delete this subscriber?"
      @close="hideDeleteModal"
      @confirm="deleteSubscriber"
    />

    <!-- Toast Notification -->
    <toast-notification ref="toast" />
  </div>
</template>

<script>
import AddEditSubscriberModal from './AddEditSubscriberModal.vue';
import ConfirmationModal from './ConfirmationModal.vue';
import magazineSubscriberService from '../services/magazineSubscriberService';

export default {
  components: {
    AddEditSubscriberModal,
    ConfirmationModal
  },
  data() {
    return {
      currentSubscribers: [],
      waitingForRenewalSubscribers: [],
      inactiveSubscribers: [],
      categories: [],
      types: [],
      showAddEditSubscriberModal: false,
      selectedSubscriber: null,
      showConfirmationModal: false,
      subscriberToDelete: null
    };
  },
  created() {
    this.loadSubscribers();
    this.loadCategories();
    this.loadTypes();
  },
  methods: {
    loadSubscribers() {
      magazineSubscriberService.getMagazineSubscribers().then(response => {
        this.currentSubscribers = response.data.filter(subscriber => !subscriber.isDeleted && subscriber.hasActiveSubscriptions);
        this.waitingForRenewalSubscribers = response.data.filter(subscriber => !subscriber.isDeleted && !subscriber.hasActiveSubscriptions);
        this.inactiveSubscribers = response.data.filter(subscriber => subscriber.isDeleted);
      }).catch(error => {
        console.error("There was an error retrieving the subscribers!", error);
      });
    },
    loadCategories() {
      magazineSubscriberService.getCategories().then(response => {
        this.categories = response.data;
      }).catch(error => {
        console.error("There was an error retrieving the categories!", error);
      });
    },
    loadTypes() {
      magazineSubscriberService.getTypes().then(response => {
        this.types = response.data;
      }).catch(error => {
        console.error("There was an error retrieving the types!", error);
      });
    },
    openAddSubscriberModal() {
      this.selectedSubscriber = {
        name: '',
        registration_number: '',
        address: '',
        city_town: '',
        state: '',
        pincode: '',
        phone: '',
        email: '',
        category: '',
        stype: '',
        notes: ''
      };
      this.showAddEditSubscriberModal = true;
    },
    openEditSubscriberModal(subscriber) {
      this.selectedSubscriber = { ...subscriber };
      this.showAddEditSubscriberModal = true;
    },
    closeAddEditSubscriberModal() {
      this.showAddEditSubscriberModal = false;
    },
    saveSubscriber(subscriber) {
      if (subscriber._id) {
        magazineSubscriberService.updateMagazineSubscriber(subscriber._id, subscriber).then(() => {
          this.loadSubscribers();
          this.showAddEditSubscriberModal = false;
        }).catch(error => {
          console.error("There was an error updating the subscriber!", error);
        });
      } else {
        magazineSubscriberService.createMagazineSubscriber(subscriber).then(() => {
          this.loadSubscribers();
          this.showAddEditSubscriberModal = false;
        }).catch(error => {
          console.error("There was an error adding the subscriber!", error);
        });
      }
    },
    confirmDeleteSubscriber(subscriberId) {
      this.subscriberToDelete = subscriberId;
      this.showConfirmationModal = true;
    },
    hideDeleteModal() {
      this.showConfirmationModal = false;
    },
    deleteSubscriber() {
      if (this.subscriberToDelete) {
        magazineSubscriberService.softDeleteMagazineSubscriber(this.subscriberToDelete).then(() => {
          this.loadSubscribers();
          this.hideDeleteModal();
        }).catch(error => {
          console.error("There was an error deleting the subscriber!", error);
        });
      }
    },
    activateSubscriber(subscriberId) {
      magazineSubscriberService.activateMagazineSubscriber(subscriberId).then(() => {
        this.loadSubscribers();
      }).catch(error => {
        console.error("There was an error activating the subscriber!", error);
      });
    },
    viewSubscriber(subscriberId) {
      this.$router.push({ name: 'SubscriberDetails', params: { id: subscriberId } });
    }
  }
};
</script>

<style scoped>
.table {
  margin-top: 20px;
}
</style>
