<script lang="ts">
  import { createEventDispatcher } from "svelte";
  import InputNumber from "./InputNumber.svelte";
  import InputCheckbox from "./InputCheckbox.svelte";
  import Select from "./Select.svelte";

  const dispatch = createEventDispatcher();

  export let url = "";
  export let width = 1920;
  export let height = 1080;
  export let browser = "firefox";
  export let fullPage = true;

  const handleSubmit = (e: Event) => {
    const form = e.target as HTMLFormElement;

    if (!form.checkValidity()) return;

    e.preventDefault();

    dispatch("submit", { url, width, height, browser, "full-page": fullPage });
  };
</script>

<form class="form" on:submit={handleSubmit}>
  <div class="url">
    <input
      class="url__input"
      type="url"
      name="url"
      bind:value={url}
      aria-label="Url to screenshot"
      placeholder="https://example.com"
      required
    />
    <button class="url__submit" type="submit">Screenshot ✨</button>
  </div>

  <div class="options">
    <InputNumber
      bind:value={width}
      max={3000}
      min={320}
      slug="width"
      label="Width"
    />

    <InputNumber
      bind:value={height}
      max={3000}
      min={320}
      slug="height"
      label="Height"
    />

    <Select
      bind:value={browser}
      slug="browser-type"
      label="Browser"
      options={["chromium", "firefox", "webkit"]}
    />

    <InputCheckbox bind:checked={fullPage} slug="full-page" label="Full Page" />
  </div>
</form>

<style lang="scss">
  .form {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    margin-bottom: 3rem;
  }

  .url {
    display: grid;
    grid-template-columns: 1fr;

    @media screen and (min-width: 800px) {
      grid-template-columns: 4fr 1fr;
    }

    &__input {
      background-color: var(--secondary-color);
      padding: 0.75rem 1.25rem;
      border: 2px solid transparent;
      border-top-left-radius: 0.25rem;
      border-top-right-radius: 0.25rem;
      transition: border-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out;

      @media screen and (min-width: 800px) {
        padding: 0.5rem 1rem;
        border-top-right-radius: 0;
        border-bottom-left-radius: 0.25rem;
      }

      &:focus {
        border-color: var(--element-color);
        box-shadow: 0 0 5px var(--element-color);
      }
    }

    &__submit {
      background-color: var(--element-color);
      padding: 0.75rem 1.25rem;
      font-weight: bold;
      color: var(--primary-color);
      border-bottom-left-radius: 0.25rem;
      border-bottom-right-radius: 0.25rem;

      @media screen and (min-width: 800px) {
        border-top-right-radius: 0.25rem;
        border-bottom-left-radius: 0;
      }

      @media (hover: hover) {
        transition: transform 0.2s;

        &:hover {
          transform: scale(1.01);
          box-shadow: 0 0 5px var(--element-color);
        }
      }
    }
  }

  .options {
    display: grid;
    grid-template-columns: 1fr;
    gap: 1rem;

    @media screen and (min-width: 900px) {
      grid-template-columns: repeat(2, 200px) 225px 1fr;
    }
  }
</style>
