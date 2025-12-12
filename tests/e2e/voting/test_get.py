# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import re

from playwright.sync_api import Page, expect


def test_body_textarea_change_updates_preview(page_voting: Page) -> None:
    """Changing the body textarea should update the preview after debounce."""
    preview_content = page_voting.locator("#vote-body-preview-content")
    body_textarea = page_voting.locator("textarea#body")

    initial_preview = preview_content.text_content()

    unique_marker = "UNIQUE_MARKER"
    body_textarea.fill(unique_marker)

    expect(preview_content).to_contain_text(unique_marker, timeout=2000)

    final_preview = preview_content.text_content()
    assert initial_preview != final_preview


def test_body_textarea_exists(page_voting: Page) -> None:
    """The body textarea should exist."""
    body_textarea = page_voting.locator("textarea#body")
    expect(body_textarea).to_be_visible()


def test_initial_preview_loads_on_page_load(page_voting: Page) -> None:
    """The preview should load automatically when the page loads."""
    preview_content = page_voting.locator("#vote-body-preview-content")
    expect(preview_content).not_to_have_text("Loading preview...")


def test_preview_content_element_exists(page_voting: Page) -> None:
    """The vote body preview content element should exist."""
    preview_content = page_voting.locator("#vote-body-preview-content")
    expect(preview_content).to_be_attached()


def test_preview_tab_shows_preview_content(page_voting: Page) -> None:
    """Clicking the Text preview tab should show the preview pane."""
    preview_tab = page_voting.locator("#preview-vote-body-tab")
    preview_pane = page_voting.locator("#preview-vote-body-pane")

    preview_tab.click()

    expect(preview_pane).to_have_class(re.compile(r".*\bshow\b.*"))
    expect(preview_pane).to_have_class(re.compile(r".*\bactive\b.*"))


def test_vote_config_element_exists(page_voting: Page) -> None:
    """The vote config element should exist with required data attributes."""
    config_element = page_voting.locator("#vote-config")
    expect(config_element).to_be_attached()
    expect(config_element).to_have_attribute("data-preview-url", re.compile(r".+"))
    expect(config_element).to_have_attribute("data-min-hours", re.compile(r"\d+"))


def test_vote_duration_change_updates_preview(page_voting: Page) -> None:
    """Changing the vote duration should update the preview after debounce."""
    preview_content = page_voting.locator("#vote-body-preview-content")
    vote_duration = page_voting.locator("input#vote_duration")

    initial_preview = preview_content.text_content()

    vote_duration.fill("168")

    page_voting.wait_for_timeout(1000)

    final_preview = preview_content.text_content()
    # This assumes that the vote duration is in the default template
    assert initial_preview != final_preview


def test_vote_duration_input_exists(page_voting: Page) -> None:
    """The vote duration input should exist."""
    vote_duration = page_voting.locator("input#vote_duration")
    expect(vote_duration).to_be_visible()
